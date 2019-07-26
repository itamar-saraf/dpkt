from . import dpkt


#for development only!!!
# https://datatracker.ietf.org/doc/draft-ietf-quic-transport/?include_text=1

# Frame types

QUIC_FRAME_PADDING = 0x00
QUIC_PING = 0x01
QUIC_ACK = 0x02 - 0x03  # check this!!!
QUIC_RESET_STREAM = 0x04
QUIC_STOP_SENDING = 0x05
QUIC_CRYPTO = 0x06
QUIC_NEW_TOKEN = 0x07
QUIC_STREAM = 0x08 - 0x0f  # check this!!!
QUIC_MAX_DATA = 0x10
QUIC_MAX_STREAM_DATA = 0x11
QUIC_MAX_STREAMS = 0x12 - 0x13  # check this!!!
QUIC_DATA_BLOCKED = 0x14
QUIC_STREAM_DATA_BLOCKED = 0x15
QUIC_STREAMS_BLOCKED = 0x16 - 0x17  # check this!!!
QUIC_NEW_CONNECTION_ID = 0x18
QUIC_RETIRE_CONNECTION_ID = 0x19
QUIC_PATH_CHALLENGE = 0x1a
QUIC_PATH_RESPONSE = 0x1b
QUIC_CONNECTION_CLOSE = 0x1c - 0x1d   # check this!!!h


# Error codes

QUIC_NO_ERROR = 0x0
QUIC_INTERNAL_ERROR = 0x1
QUIC_SERVER_BUSY = 0x2
QUIC_FLOW_CONTROL_ERROR = 0x3
QUIC_STREAM_LIMIT_ERROR = 0x4
QUIC_STREAM_STATE_ERROR = 0x5
QUIC_FINAL_SIZE_ERROR = 0x6
QUIC_FRAME_ENCODING_ERROR = 0x7
QUIC_TRANSPORT_PARAMETER_ERROR = 0x8
QUIC_PROTOCOL_VIOLATION = 0xA
QUIC_INVALID_MIGRATION = 0xC

error_code_str = {
    QUIC_NO_ERROR: "No error",
    QUIC_INTERNAL_ERROR: "Implementation error",
    QUIC_SERVER_BUSY: "Server currently busy",
    QUIC_FLOW_CONTROL_ERROR: "Flow control error",
    QUIC_STREAM_LIMIT_ERROR: "Too many streams opened",
    QUIC_STREAM_STATE_ERROR: "Frame received in invalid stream state",
    QUIC_FINAL_SIZE_ERROR: "Change to final size",
    QUIC_FRAME_ENCODING_ERROR: "Frame encoding error",
    QUIC_TRANSPORT_PARAMETER_ERROR: "Error in transport parameters",
    QUIC_PROTOCOL_VIOLATION: "Generic protocol violation",
    QUIC_INVALID_MIGRATION: "Violated disabled migration",
}


class QUIC(dpkt.Packet):


    pass