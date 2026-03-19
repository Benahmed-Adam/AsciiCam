from asciiRenderer import ascii_renderer
import sys   

def main():
    if len(sys.argv) < 4:
        print("Usage: python main.py <mode: cam|vid> <color: 0|1> <opti: 0|1>")
        print("Example: python main.py cam 1 1")
        return

    mode = sys.argv[1]
    use_color = sys.argv[2] == "1"
    use_opti = sys.argv[3] == "1"

    try:
        if mode not in ["vid", "cam"]:
            raise ValueError("Mode must be either 'vid' or 'cam'")

        renderer = ascii_renderer(mode, couleur=use_color, opti=use_opti)
        renderer.run()

    except Exception as e:
        print(f"Error : {e}")
        print("Example : python ./main.py cam 1 1")

if __name__ == "__main__":
    main()