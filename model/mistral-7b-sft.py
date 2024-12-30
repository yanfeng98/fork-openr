from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "peiyi9979/mistral-7b-sft"
device = "cuda:7" # the device to load the model onto

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map=device
)
tokenizer = AutoTokenizer.from_pretrained(model_name)