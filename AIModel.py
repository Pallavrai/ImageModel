from transformers import AutoProcessor, PaliGemmaForConditionalGeneration
from PIL import Image
import requests
import torch


def run_model(image: Image.Image, prompt: str,train_on):
    model_id = "google/paligemma-3b-mix-224"
    device = train_on
    dtype = torch.bfloat16

    model = PaliGemmaForConditionalGeneration.from_pretrained(
        model_id,
        torch_dtype=dtype,
        device_map=device,
        revision="bfloat16",
    ).eval()
    processor = AutoProcessor.from_pretrained(model_id)

    model_inputs = processor(text=prompt, images=image, return_tensors="pt").to(model.device)
    input_len = model_inputs["input_ids"].shape[-1]

    with torch.inference_mode():
        generation = model.generate(**model_inputs, max_new_tokens=100, do_sample=False)
        generation = generation[0][input_len:]
        decoded = processor.decode(generation, skip_special_tokens=True)
        return str(decoded)
# def run_model(url:str,prompt:str):
#     model_id = "google/paligemma-3b-mix-224"
#     device = "mps"
#     dtype = torch.bfloat16

#     # url = "https://images.ctfassets.net/hrltx12pl8hq/28ECAQiPJZ78hxatLTa7Ts/2f695d869736ae3b0de3e56ceaca3958/free-nature-images.jpg?fit=fill&w=1200&h=630"
#     # image = Image.open(requests.get(url, stream=True).raw)
#     image = Image.open(url)

#     model = PaliGemmaForConditionalGeneration.from_pretrained(
#         model_id,
#         torch_dtype=dtype,
#         device_map=device,
#         revision="bfloat16",
#     ).eval()
#     processor = AutoProcessor.from_pretrained(model_id)


#     # prompt = "what is the colour of tree"
#     model_inputs = processor(text=prompt, images=image, return_tensors="pt").to(model.device)
#     input_len = model_inputs["input_ids"].shape[-1]

#     with torch.inference_mode():
#         generation = model.generate(**model_inputs, max_new_tokens=100, do_sample=False)
#         generation = generation[0][input_len:]
#         decoded = processor.decode(generation, skip_special_tokens=True)
#         return str(decoded)
