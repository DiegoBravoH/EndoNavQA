GastroHUN Installation
=======================

1. **Dependencies:**
  The codebase primarily uses the following libraries:
   - **Python**: Version 3.10 or newer.
   - **PyTorch and torchvision**: Essential for reproducing the main results. The setup has been tested successfully with the following configurations:
   - CUDA >= 11.8
   - PyTorch >= 1.8.0
   - torchvision >= 0.18.1
   - torch >= 2.3.1+cu121
  
  ```bash
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124 
    pip install "vllm>=0.11.0"
    pip install flashinfer  
    pip install "transformers>=4.45.0" "accelerate>=0.31.0"  
  ```
  2. **deepseek:**
  ```bash
    git clone https://github.com/deepseek-ai/Janus.git 
    cd Janus
  pip install -e .
  ```
  3. **llama:**
  ```bash
    import transformers
    import torch

    model_id = "meta-llama/Meta-Llama-3-8B-Instruct"

    pipeline = transformers.pipeline(
      "text-generation",
      model="meta-llama/Meta-Llama-3-8B-Instruct",
      model_kwargs={"torch_dtype": torch.bfloat16},
      device="cuda",
    )
  ```
  4. **GTP-4o:**
