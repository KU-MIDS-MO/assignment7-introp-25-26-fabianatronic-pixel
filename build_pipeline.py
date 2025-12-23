def build_pipeline(operation_names):
    
    valid_ops = {"add_one", "double", "triple", "square"}
    
    for op in operation_names:
        if op not in valid_ops:
            raise KeyError (op)
            
    def pipeline(x):
        result = x
        
        for op in operation_names:
            if op == "add_one":
                result = result + 1
            elif op == "double":
                result = result * 2 
            elif op == "triple":
                result = result *3
            elif op == "square":
                result = result **2
            
                
        return result
    
    return pipeline
