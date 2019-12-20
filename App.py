from view.PantallaPrincipal import PantallaPrincipal
from ControlArranque import ControladorArranque


def main():
    root = PantallaPrincipal()
    controller = ControladorArranque(root)
    root.mainloop()


if __name__ == '__main__':
    main()
