
/*
      -- 1 --
     |       |
     6       2
     |       |
      -- 7 --
     |       |
     5       3
     |       |
      -- 4 --
*/

module seg7 (
    input wire [3:0] counter,
    output reg [6:0] segments
);

    always @(*) begin
        case(counter)
            0:  segments = 7'b0111001;
            1:  segments = 7'b0000100;
            2:  segments = 7'b1011001;
            3:  segments = 7'b1001111;
            4:  segments = 7'b1100000;
            5:  segments = 7'b1101101;
            6:  segments = 7'b1111101;
            7:  segments = 7'b0000111;
	    default:
                segments = 7'b0000000;
        endcase
    end

endmodule

