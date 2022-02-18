import argparse

from polyaxon.client import RunClient

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--project", type=str)
    parser.add_argument("--name", type=str)
    args = parser.parse_args()

    project = args.project
    name = args.name

    client = RunClient()

    uuid = client.list(
        query=f"project.name:{project}, name:{name}", sort="-metrics.accuracy", limit=1
    )

    print(uuid, end='')
