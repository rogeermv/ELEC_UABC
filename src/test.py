import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles


segments = [ 57, 4, 89, 79, 96, 109, 125, 7 ]

@cocotb.test()
async def test_7seg(dut):
    dut._log.info("start")
    clock = Clock(dut.clk, 1, units="ms")
    cocotb.start_soon(clock.start())

    # reset
    dut._log.info("reset")
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 1)
    dut.rst_n.value = 1

    # check all segments and roll over
    dut._log.info("check all segments")
    for i in range(8):
        dut._log.info("check segment {}".format(i))
        await ClockCycles(dut.clk, 1000)

        
        assert dut.uio_oe == 0xFF

