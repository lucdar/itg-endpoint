PROTO_DIR = ./proto
PROTO = ./proto/itg_buddy.proto
OUT_DIR = ./src/itg_buddy_endpoint/rpc

rpc:
	uv run -m grpc_tools.protoc -I "$(PROTO_DIR)" --python_out="$(OUT_DIR)" --grpc_python_out="$(OUT_DIR)" "$(PROTO)"
