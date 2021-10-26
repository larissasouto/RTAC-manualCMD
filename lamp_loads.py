from pymodbus.client.sync import ModbusTcpClient
import RPi.GPIO as GPIO
import time

# server connection
server_ip_address = '127.0.0.1'
server_port = 10502

client = ModbusTcpClient(server_ip_address, server_port)

print("[+]Info : Connection : " + str(client.connect()))

UNIT = 2
# server connection

# Rpi pin definition
relay1 = 29
relay2 = 31
relay3 = 33
relay4 = 36
relay5 = 35
relay6 = 38
relay7 = 40

# Pin Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)
GPIO.setup(relay3, GPIO.OUT)
GPIO.setup(relay4, GPIO.OUT)
GPIO.setup(relay5, GPIO.OUT)
GPIO.setup(relay6, GPIO.OUT)
GPIO.setup(relay7, GPIO.OUT)

# initial states Load 1
prevRTAC_C1 = 1
nextRTAC_C1 = 1
prevManual_S1 = 1
nextManual_S1 = 1
prevFlipFlop_L1 = 1
nextFlipFlop_L1 = 1

# initial states Load 2
prevRTAC_C2 = 1
nextRTAC_C2 = 1
prevManual_S2 = 1
nextManual_S2 = 1
prevFlipFlop_L2 = 1
nextFlipFlop_L2 = 1

# initial states Load 3
prevRTAC_C3 = 1
nextRTAC_C3 = 1
prevManual_S3 = 1
nextManual_S3 = 1
prevFlipFlop_L3 = 1
nextFlipFlop_L3 = 1

# initial states Load 4
prevRTAC_C4 = 1
nextRTAC_C4 = 1
prevManual_S4 = 1
nextManual_S4 = 1
prevFlipFlop_L4 = 1
nextFlipFlop_L4 = 1

# initial states Load 5
prevRTAC_C5 = 1
nextRTAC_C5 = 1
prevManual_S5 = 1
nextManual_S5 = 1
prevFlipFlop_L5 = 1
nextFlipFlop_L5 = 1

# initial states Load 6
prevRTAC_C6 = 1
nextRTAC_C6 = 1
prevManual_S6 = 1
nextManual_S6 = 1
prevFlipFlop_L6 = 1
nextFlipFlop_L6 = 1

# initial states Load 7
prevRTAC_C7 = 1
nextRTAC_C7 = 1
prevManual_S7 = 1
nextManual_S7 = 1
prevFlipFlop_L7 = 1
nextFlipFlop_L7 = 1


# LOGIC FUNCTIONS
""" Pset control mode """


def pset_mode(value):
    print("PSET CONTROL MODE")
    pset_power = value.registers[0]

    if pset_power < 828:
        print("S1 OFF\nS2 OFF\nS3 OFF\nS4 OFF\nS5 OFF\nS6 OFF\nS7 OFF\n")
        GPIO.output(relay1, 1)
        GPIO.output(relay2, 1)
        GPIO.output(relay3, 1)
        GPIO.output(relay4, 1)
        GPIO.output(relay5, 1)
        GPIO.output(relay6, 1)
        GPIO.output(relay7, 1)

        client.write_coils(9, [1] * 7, unit=UNIT)  # RTAC loads state (OFF)

    if (pset_power >= 828) and (pset_power < 1656):
        print("S1 ON\nS2 OFF\nS3 OFF\nS4 OFF\nS5 OFF\nS6 OFF\nS7 OFF\n")
        GPIO.output(relay1, 0)
        GPIO.output(relay2, 1)
        GPIO.output(relay3, 1)
        GPIO.output(relay4, 1)
        GPIO.output(relay5, 1)
        GPIO.output(relay6, 1)
        GPIO.output(relay7, 1)

        client.write_coil(9, 0, unit=UNIT)  # RTAC loads state (ON)
        client.write_coils(10, [1] * 6, unit=UNIT)  # RTAC loads state (OFF)

    if (pset_power >= 1656) and (pset_power < 2484):
        print("S1 ON\nS2 ON\nS3 OFF\nS4 OFF\nS5 OFF\nS6 OFF\nS7 OFF\n")
        GPIO.output(relay1, 0)
        GPIO.output(relay2, 0)
        GPIO.output(relay3, 1)
        GPIO.output(relay4, 1)
        GPIO.output(relay5, 1)
        GPIO.output(relay6, 1)
        GPIO.output(relay7, 1)

        client.write_coils(9, [0] * 2, unit=UNIT)  # RTAC loads state (ON)
        client.write_coils(11, [1] * 5, unit=UNIT)  # RTAC loads state (OFF)

    if (pset_power >= 2484) and (pset_power < 3312):
        print("S1 ON\nS2 ON\nS3 ON\nS4 OFF\nS5 OFF\nS6 OFF\nS7 OFF\n")
        GPIO.output(relay1, 0)
        GPIO.output(relay2, 0)
        GPIO.output(relay3, 0)
        GPIO.output(relay4, 1)
        GPIO.output(relay5, 1)
        GPIO.output(relay6, 1)
        GPIO.output(relay7, 1)

        client.write_coils(9, [0] * 3, unit=UNIT)  # RTAC loads state (ON)
        client.write_coils(12, [1] * 4, unit=UNIT)  # RTAC loads state (OFF)

    if (pset_power >= 3312) and (pset_power < 4140):
        print("S1 ON\nS2 ON\nS3 ON\nS4 ON\nS5 OFF\nS6 OFF\nS7 OFF\n")
        GPIO.output(relay1, 0)
        GPIO.output(relay2, 0)
        GPIO.output(relay3, 0)
        GPIO.output(relay4, 0)
        GPIO.output(relay5, 1)
        GPIO.output(relay6, 1)
        GPIO.output(relay7, 1)

        client.write_coils(9, [0] * 4, unit=UNIT)  # RTAC loads state (ON)
        client.write_coils(13, [1] * 3, unit=UNIT)  # RTAC loads state (OFF)

    if (pset_power >= 4140) and (pset_power < 4968):
        print("S1 ON\nS2 ON\nS3 ON\nS4 ON\nS5 ON\nS6 OFF\nS7 OFF\n")
        GPIO.output(relay1, 0)
        GPIO.output(relay2, 0)
        GPIO.output(relay3, 0)
        GPIO.output(relay4, 0)
        GPIO.output(relay5, 0)
        GPIO.output(relay6, 1)
        GPIO.output(relay7, 1)

        client.write_coils(9, [0] * 5, unit=UNIT)  # RTAC loads state (ON)
        client.write_coils(14, [1] * 2, unit=UNIT)  # RTAC loads state (OFF)

    if (pset_power >= 4968) and (pset_power < 5796):
        print("S1 ON\nS2 ON\nS3 ON\nS4 ON\nS5 ON\nS6 ON\nS7 OFF\n")
        GPIO.output(relay1, 0)
        GPIO.output(relay2, 0)
        GPIO.output(relay3, 0)
        GPIO.output(relay4, 0)
        GPIO.output(relay5, 0)
        GPIO.output(relay6, 0)
        GPIO.output(relay7, 1)

        client.write_coils(9, [0] * 6, unit=UNIT)  # RTAC loads state (ON)
        client.write_coil(15, 1, unit=UNIT)  # RTAC loads state (OFF)

    if pset_power >= 5796:
        print("S1 ON\nS2 ON\nS3 ON\nS4 ON\nS5 ON\nS6 ON\nS7 ON\n")
        GPIO.output(relay1, 0)
        GPIO.output(relay2, 0)
        GPIO.output(relay3, 0)
        GPIO.output(relay4, 0)
        GPIO.output(relay5, 0)
        GPIO.output(relay6, 0)
        GPIO.output(relay7, 0)

        client.write_coils(9, [0] * 7, unit=UNIT)  # RTAC loads state (ON)
        state = GPIO.input(relay7)


def risingEdgeDetector(prevState, nextState):
    if prevState < nextState:
        return 1
    return 0


def fallingEdgeDetector(prevState, nextState):
    if prevState > nextState:
        return 1
    return 0


def srFlipFlop(s, r, prevFlipFlop, nextFlipFlop):
    # SR flip-flop truth table implementation
    if s == 0 and r == 0:
        nextFlipFlop = prevFlipFlop
    elif s == 0 and r == 1:
        nextFlipFlop = 0
    elif s == 1 and r == 0:
        nextFlipFlop = 1
    else:
        nextFlipFlop = prevFlipFlop

    return nextFlipFlop


def orLogic(RTAC, manual):
    if RTAC == 0 and manual == 1:
        return 1
    if RTAC == 1 and manual == 0:
        return 1
    return 0


""" RTAC control mode """


def rtac_mode(values, load):
    # initial states Load 1
    global prevRTAC_C1, nextRTAC_C1, prevManual_S1, nextManual_S1, prevFlipFlop_L1, prevFlipFlop_L1

    # initial states Load 2
    global prevRTAC_C2, nextRTAC_C2, prevManual_S2, nextManual_S2, prevFlipFlop_L2, prevFlipFlop_L2

    # initial states Load 3
    global prevRTAC_C3, nextRTAC_C3, prevManual_S3, nextManual_S3, prevFlipFlop_L3, prevFlipFlop_L3

    # initial states Load 4
    global prevRTAC_C4, nextRTAC_C4, prevManual_S4, nextManual_S4, prevFlipFlop_L4, prevFlipFlop_L4

    # initial states Load 5
    global prevRTAC_C5, nextRTAC_C5, prevManual_S5, nextManual_S5, prevFlipFlop_L5, prevFlipFlop_L5

    # initial states Load 6
    global prevRTAC_C6, nextRTAC_C6, prevManual_S6, nextManual_S6, prevFlipFlop_L6, prevFlipFlop_L6

    # initial states Load 7
    global prevRTAC_C7, nextRTAC_C7, prevManual_S7, nextManual_S7, prevFlipFlop_L7, prevFlipFlop_L7

    if load == 1:
        prevRTAC_C1 = nextRTAC_C1
        response_RTAC = values.bits[0]  # coil 2 - S1 cmd
        nextRTAC_C1 = response_RTAC

        prevManual_S1 = nextManual_S1
        response_Manual = client.read_holding_registers(1, 1, unit=UNIT)  # HR 1 - C1 cmd (simulation)
#        nextManual_S1 = response_Manual.registers[0]
        nextManual_S1 = GPIO.input(relay1)

        risingEdgeRTAC = risingEdgeDetector(prevRTAC_C1, nextRTAC_C1)
        risingEdgeManual = risingEdgeDetector(prevManual_S1, nextManual_S1)

        fallingEdgeRTAC = fallingEdgeDetector(prevRTAC_C1, nextRTAC_C1)
        fallingEdgeManual = fallingEdgeDetector(prevManual_S1, nextManual_S1)

        # OR Logic
        s = orLogic(risingEdgeRTAC, risingEdgeManual)
        r = orLogic(fallingEdgeRTAC, fallingEdgeManual)

        global prevFlipFlop_L1, nextFlipFlop_L1
        prevFlipFlop_L1 = nextFlipFlop_L1

        loadState = srFlipFlop(s, r, prevFlipFlop_L1, nextFlipFlop_L1)
        nextFlipFlop_L1 = loadState

        GPIO.output(relay1, loadState)
        client.write_coil(9, loadState, unit=UNIT)
        return loadState

    if load == 2:
        prevRTAC_C2 = nextRTAC_C2
        response_RTAC = values.bits[1]  # coil 3 - S2 cmd
        nextRTAC_C2 = response_RTAC

        prevManual_S2 = nextManual_S2
        response_Manual = client.read_holding_registers(2, 1, unit=UNIT)  # HR 2 - C2 cmd (simulation)
#        nextManual_S2 = response_Manual.registers[0]
        nextManual_S2 = GPIO.input(relay2)

        risingEdgeRTAC = risingEdgeDetector(prevRTAC_C2, nextRTAC_C2)
        risingEdgeManual = risingEdgeDetector(prevManual_S2, nextManual_S2)

        fallingEdgeRTAC = fallingEdgeDetector(prevRTAC_C2, nextRTAC_C2)
        fallingEdgeManual = fallingEdgeDetector(prevManual_S2, nextManual_S2)

        # OR Logic
        s = orLogic(risingEdgeRTAC, risingEdgeManual)
        r = orLogic(fallingEdgeRTAC, fallingEdgeManual)

        global prevFlipFlop_L2, nextFlipFlop_L2
        prevFlipFlop_L2 = nextFlipFlop_L2

        loadState = srFlipFlop(s, r, prevFlipFlop_L2, nextFlipFlop_L2)
        nextFlipFlop_L2 = loadState

        GPIO.output(relay2, loadState)
        client.write_coil(10, loadState, unit=UNIT)
        return loadState

    if load == 3:
        prevRTAC_C3 = nextRTAC_C3
        response_RTAC = values.bits[2]  # coil 4 - S3 cmd
        nextRTAC_C3 = response_RTAC

        prevManual_S3 = nextManual_S3
        response_Manual = client.read_holding_registers(3, 1, unit=UNIT)  # HR 3 - C3 cmd (simulation)
#        nextManual_S3 = response_Manual.registers[0]
        nextManual_S3 = GPIO.input(relay3)

        risingEdgeRTAC = risingEdgeDetector(prevRTAC_C3, nextRTAC_C3)
        risingEdgeManual = risingEdgeDetector(prevManual_S3, nextManual_S3)

        fallingEdgeRTAC = fallingEdgeDetector(prevRTAC_C3, nextRTAC_C3)
        fallingEdgeManual = fallingEdgeDetector(prevManual_S3, nextManual_S3)

        # OR Logic
        s = orLogic(risingEdgeRTAC, risingEdgeManual)
        r = orLogic(fallingEdgeRTAC, fallingEdgeManual)

        global prevFlipFlop_L3, nextFlipFlop_L3
        prevFlipFlop_L3 = nextFlipFlop_L3

        loadState = srFlipFlop(s, r, prevFlipFlop_L3, nextFlipFlop_L3)
        nextFlipFlop_L3 = loadState

        GPIO.output(relay3, loadState)
        client.write_coil(11, loadState, unit=UNIT)
        return loadState

    if load == 4:
        prevRTAC_C4 = nextRTAC_C4
        response_RTAC = values.bits[3]  # coil 5 - S4 cmd
        nextRTAC_C4 = response_RTAC

        prevManual_S4 = nextManual_S4
        response_Manual = client.read_holding_registers(4, 1, unit=UNIT)  # HR 4 - C4 cmd (simulation)
#        nextManual_S4 = response_Manual.registers[0]
        nextManual_S4 = GPIO.input(relay4)

        risingEdgeRTAC = risingEdgeDetector(prevRTAC_C4, nextRTAC_C4)
        risingEdgeManual = risingEdgeDetector(prevManual_S4, nextManual_S4)

        fallingEdgeRTAC = fallingEdgeDetector(prevRTAC_C4, nextRTAC_C4)
        fallingEdgeManual = fallingEdgeDetector(prevManual_S4, nextManual_S4)

        # OR Logic
        s = orLogic(risingEdgeRTAC, risingEdgeManual)
        r = orLogic(fallingEdgeRTAC, fallingEdgeManual)

        global prevFlipFlop_L4, nextFlipFlop_L4
        prevFlipFlop_L4 = nextFlipFlop_L4

        loadState = srFlipFlop(s, r, prevFlipFlop_L4, nextFlipFlop_L4)
        nextFlipFlop_L4 = loadState

        GPIO.output(relay4, loadState)
        client.write_coil(12, loadState, unit=UNIT)
        return loadState

    if load == 5:
        prevRTAC_C5 = nextRTAC_C5
        response_RTAC = values.bits[4]  # coil 6 - S5 cmd
        nextRTAC_C5 = response_RTAC

        prevManual_S5 = nextManual_S5
        response_Manual = client.read_holding_registers(5, 1, unit=UNIT)  # HR 5 - C5 cmd (simulation)
#        nextManual_S5 = response_Manual.registers[0]
        nextManual_S5 = GPIO.input(relay5)

        risingEdgeRTAC = risingEdgeDetector(prevRTAC_C5, nextRTAC_C5)
        risingEdgeManual = risingEdgeDetector(prevManual_S5, nextManual_S5)

        fallingEdgeRTAC = fallingEdgeDetector(prevRTAC_C5, nextRTAC_C5)
        fallingEdgeManual = fallingEdgeDetector(prevManual_S5, nextManual_S5)

        # OR Logic
        s = orLogic(risingEdgeRTAC, risingEdgeManual)
        r = orLogic(fallingEdgeRTAC, fallingEdgeManual)

        global prevFlipFlop_L5, nextFlipFlop_L5
        prevFlipFlop_L5 = nextFlipFlop_L5

        loadState = srFlipFlop(s, r, prevFlipFlop_L5, nextFlipFlop_L5)
        nextFlipFlop_L5 = loadState

        GPIO.output(relay5, loadState)
        client.write_coil(13, loadState, unit=UNIT)
        return loadState

    if load == 6:
        prevRTAC_C6 = nextRTAC_C6
        response_RTAC = values.bits[5]  # coil 7 - S6 cmd
        nextRTAC_C6 = response_RTAC

        prevManual_S6 = nextManual_S6
        response_Manual = client.read_holding_registers(6, 1, unit=UNIT)  # HR 6 - C6 cmd (simulation)
#        nextManual_S6 = response_Manual.registers[0]
        nextManual_S6 = GPIO.input(relay6)

        risingEdgeRTAC = risingEdgeDetector(prevRTAC_C6, nextRTAC_C6)
        risingEdgeManual = risingEdgeDetector(prevManual_S6, nextManual_S6)

        fallingEdgeRTAC = fallingEdgeDetector(prevRTAC_C6, nextRTAC_C6)
        fallingEdgeManual = fallingEdgeDetector(prevManual_S6, nextManual_S6)

        # OR Logic
        s = orLogic(risingEdgeRTAC, risingEdgeManual)
        r = orLogic(fallingEdgeRTAC, fallingEdgeManual)

        global prevFlipFlop_L6, nextFlipFlop_L6
        prevFlipFlop_L6 = nextFlipFlop_L6

        loadState = srFlipFlop(s, r, prevFlipFlop_L6, nextFlipFlop_L6)
        nextFlipFlop_L6 = loadState

        GPIO.output(relay6, loadState)
        client.write_coil(14, loadState, unit=UNIT)
        return loadState

    if load == 7:
        prevRTAC_C7 = nextRTAC_C7
        response_RTAC = values.bits[6]  # coil 8 - S7 cmd
        nextRTAC_C7 = response_RTAC

        prevManual_S7 = nextManual_S7
        response_Manual = client.read_holding_registers(7, 1, unit=UNIT)  # HR 7 - C7 cmd (simulation)
#        nextManual_S7 = response_Manual.registers[0]
        nextManual_S7 = GPIO.input(relay7)

        risingEdgeRTAC = risingEdgeDetector(prevRTAC_C7, nextRTAC_C7)
        risingEdgeManual = risingEdgeDetector(prevManual_S7, nextManual_S7)

        fallingEdgeRTAC = fallingEdgeDetector(prevRTAC_C7, nextRTAC_C7)
        fallingEdgeManual = fallingEdgeDetector(prevManual_S7, nextManual_S7)

        # OR Logic
        s = orLogic(risingEdgeRTAC, risingEdgeManual)
        r = orLogic(fallingEdgeRTAC, fallingEdgeManual)

        global prevFlipFlop_L7, nextFlipFlop_L7
        prevFlipFlop_L7 = nextFlipFlop_L7

        loadState = srFlipFlop(s, r, prevFlipFlop_L7, nextFlipFlop_L7)
        nextFlipFlop_L7 = loadState

        GPIO.output(relay7, loadState)
        client.write_coil(15, loadState, unit=UNIT)
        state = GPIO.input(relay7)
        return loadState


def getValues():
    # code here
    control_mode = client.read_coils(1, 1, unit=UNIT)

    if control_mode.bits[0] == False:
        print("RTAC CONTROL MODE")
        values = client.read_coils(2, 9, unit=UNIT)
        #  Load 1
        loadState = rtac_mode(values, 1)
        print("SWITCH 1: {I}".format(I=loadState))
        #  Load 2
        loadState = rtac_mode(values, 2)
        print("SWITCH 2: {I}".format(I=loadState))
        #  Load 3
        loadState = rtac_mode(values, 3)
        print("SWITCH 3: {I}".format(I=loadState))
        #  Load 4
        loadState = rtac_mode(values, 4)
        print("SWITCH 4: {I}".format(I=loadState))
        #  Load 5
        loadState = rtac_mode(values, 5)
        print("SWITCH 5: {I}".format(I=loadState))
        #  Load 6
        loadState = rtac_mode(values, 6)
        print("SWITCH 6: {I}".format(I=loadState))
        #  Load 7
        loadState = rtac_mode(values, 7)
        print("SWITCH 7: {I}\n".format(I=loadState))

    else:
        power_value = client.read_holding_registers(0, 1, unit=UNIT)
        pset_mode(power_value)
    time.sleep(5)  # wait 5 seconds


while True:
    getValues()

