import torch

def main():
    print("Hello from mp!")
    print(f"Torch version: {torch.__version__}")
    print(torch.cuda.is_available())
    
if __name__ == "__main__":
    main()
