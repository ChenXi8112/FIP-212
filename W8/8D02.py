"""8D02-列车倒挂"""

def reverse_train(vals):
    new_vals = []
    while vals:
        new_vals.append(vals.pop())
    return new_vals
