# Copyright 2024 luyanfeng
#
# Licensed under the MIT License, (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import random
import os
from transformers import set_seed

# Set your Hugging Face token here
os.environ["HUGGINGFACE_HUB_TOKEN"] = "hf_yourkey"

# For reproducibility
SEED = 1234
set_seed(SEED)
random.seed(42)

class LM:
    def __init__(self, model_name: str = "Qwen/Qwen2.5-Math-7B-Instruct", model_type: str = "hf", num_rollouts: int = 5, **model_args):
        self.model_type = model_type.lower()
        self.model_name = model_name
        
        self.max_tokens = 200
        self.temperature_range = [0.7, 1.0]
        self.num_rollouts = num_rollouts
        self.__dict__.update(model_args)
        print("Updated model args:", self.__dict__)
        
        if self.model_type == "hf":
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForCausalLM.from_pretrained(
                model_name, torch_dtype=torch.float16, device_map="cuda"
            )
        else:
            raise ValueError("Invalid model_type. Choose 'hf' or 'openai'.")
        
    def generate(self, question, partial_answer, num_rollouts=None):
        if num_rollouts is None:
            num_rollouts = self.num_rollouts
        prompt = question + partial_answer
        if self.model_type == "hf":
            return self.generate_hf(prompt, num_rollouts)

    def generate_hf(self, prompt, num_rollouts):
        inputs = self.tokenizer(prompt, return_tensors="pt").to('cuda')
        results = []
        for _ in range(num_rollouts):
            temperature = random.uniform(self.temperature_range[0], self.temperature_range[1])
            outputs = self.model.generate(
                **inputs, do_sample=True, max_new_tokens=self.max_tokens, temperature=temperature,
                num_return_sequences=1
            )
            generated_tokens = outputs[0][inputs['input_ids'].shape[1]:]
            result = self.tokenizer.decode(generated_tokens, skip_special_tokens=True)
            results.append(result)
        return results
