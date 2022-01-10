'''
Base case: If the expression has no symbol, i.e. its a number, then there's nothing to do. Just add to result.
Recursive case: Split the expression at every symbol and evaluate the parts recursively.
Why split at every symbol? Because its analogous to adding parantheses. e.g. 1 + 2 * 3
when split at +, parts are 1 and 2 * 3 which can be written as 1 + (2 * 3)
when split at *, parts are 1 + 2 and 3 which can be written as (1 + 2) * 3
'''
