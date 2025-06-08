from .controllers.search_controller import SearchController


def main(query: str) -> None:
    controller = SearchController()
    result = controller.search(query)
    print(result)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m src.main '<query>'")
    else:
        main(sys.argv[1])
