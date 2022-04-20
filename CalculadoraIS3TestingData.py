
operations = ["Add","Subtract","Multiply", "Divide", "Concatenate"]

errors = ["Number 1 is not a number","Number 2 is not a number", "Divide by zero error!"]

testCases = {
    "Add": [["asd","", "Number 1 is not a number"],["","asd", "Number 2 is not a number"],["aaa","bbb","Number 1 is not a number"],["?","", "Number 1 is not a number"],["","!","Number 2 is not a number"],
                ["&/","#$","Number 1 is not a number"],["asda#$%", "", "Number 1 is not a number"],["","as/(%&/(","Number 2 is not a number"],
            ["ñop%&","ññ/(/(","Number 1 is not a number"],["--3","","Number 1 is not a number"],["","--90","Number 2 is not a number"],["++7","","Number 1 is not a number"],["","++10","Number 2 is not a number"],  
            [--5,--5,"Number 1 is not a number"],["++1","++1","Number 1 is not a number"],["-+1","+-8","Number 1 is not a number"], ["","", 0]  ],
    "Subtract": [["asd","", "Number 1 is not a number"],["","asd", "Number 2 is not a number"],["aaa","bbb","Number 1 is not a number"],["?","", "Number 1 is not a number"],["","!","Number 2 is not a number"],
                ["&/","#$","Number 1 is not a number"],["asda#$%", "", "Number 1 is not a number"],["","as/(%&/(","Number 2 is not a number"],
            ["ñop%&","ññ/(/(","Number 1 is not a number"],["--3","","Number 1 is not a number"],["","--90","Number 2 is not a number"],["++7","","Number 1 is not a number"],["","++10","Number 2 is not a number"],  
            [--5,--5,"Number 1 is not a number"],["++1","++1","Number 1 is not a number"],["-+1","+-8","Number 1 is not a number"], ["","",0]],
    "Multiply": [["asd","", "Number 1 is not a number"],["","asd", "Number 2 is not a number"],["aaa","bbb","Number 1 is not a number"],["?","", "Number 1 is not a number"],["","!","Number 2 is not a number"],
                ["&/","#$","Number 1 is not a number"],["asda#$%", "", "Number 1 is not a number"],["","as/(%&/(","Number 2 is not a number"],
            ["ñop%&","ññ/(/(","Number 1 is not a number"],["--3","","Number 1 is not a number"],["","--90","Number 2 is not a number"],["++7","","Number 1 is not a number"],["","++10","Number 2 is not a number"],  
            [--5,--5,"Number 1 is not a number"],["++1","++1","Number 1 is not a number"],["-+1","+-8","Number 1 is not a number"], ["","",0]],
    "Divide": [["asd","", "Number 1 is not a number"],["","asd", "Number 2 is not a number"],["aaa","bbb","Number 1 is not a number"],["?","", "Number 1 is not a number"],["","!","Number 2 is not a number"],
                ["&/","#$","Number 1 is not a number"],["asda#$%", "", "Number 1 is not a number"],["","as/(%&/(","Number 2 is not a number"],
            ["ñop%&","ññ/(/(","Number 1 is not a number"],["--3","","Number 1 is not a number"],["","--90","Number 2 is not a number"],["++7","","Number 1 is not a number"],["","++10","Number 2 is not a number"],  
            [--5,--5,"Number 1 is not a number"],["++1","++1","Number 1 is not a number"],["-+1","+-8","Number 1 is not a number"],["99",0,"Divide by zero error!"],["","","Divide by zero error!"]],
    "Concatenate": [["ff","2ff33","ff2ff33"],[12345678910, "", 1234567891],["",11111111111,1111111111], [11111111111,12345678910,11111111111234567891]]
    }