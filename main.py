import torch

def main():
    print("Hello from mp!")
    print(f"Torch version: {torch.__version__}")
    print(torch.cuda.is_available())
    print(torch.cuda.current_device())
    
if __name__ == "__main__":
    main()
