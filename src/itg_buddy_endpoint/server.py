from concurrent import futures
import itg_cli
import grpc

import itg_buddy_pb2_grpc
import itg_buddy_pb2

from config import SINGLES, CACHE, DOWNLOADS


class SimfileManagementServicer(itg_buddy_pb2_grpc.SimfileManagementServicer):
    def AddSong(self, request, context):
        itg_cli.add_song(
            request.path_or_url,
            SINGLES,
            CACHE,
            downloads=DOWNLOADS,
            overwrite=request.overwrite,
            delete_macos_files_flag=False,
        )
        res = itg_buddy_pb2.AddSongResponse()
        res.added_song, res.destination = "cool", "beans"
        return res


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    itg_buddy_pb2_grpc.add_SimfileManagementServicer_to_server(
        SimfileManagementServicer(), server
    )
    server.add_insecure_port("localhost:50051")
    server.start()
    print("Started itg-buddy-responder!")
    server.wait_for_termination()


if __name__ == "__main__":
    main()
