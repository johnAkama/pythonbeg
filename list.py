def apply_discount(price,discount):
    if not isinstance(price,(int,float)):
        return "The price should be a number"
    else:
        if not isinstance(discount,(int,float)):
            return "The discount should be a number"
        else:
            
            if price <= 0:
                    return "The price should be greater than 0"
            else:
                if discount > 100 or discount < 0:
                        return "The discount should be between 0 and 100"
                else:
                    return (price-(price*discount)/100)

print(apply_discount (10,5))

    