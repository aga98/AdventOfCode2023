from utils import read_input


def process_input(lines: list) -> tuple:
    workflows = {}
    parts = []
    is_workflow = True
    for line in lines:
        if line == "":
            is_workflow = False
        elif is_workflow:
            w = line[:-1].split("{")
            w_name = w[0]
            w_rules = w[1].split(",")
            parsed_rules = []
            for rule in w_rules:
                if ":" in rule:
                    rule = rule.split(":")
                    condition = rule[0]
                    next_w = rule[1]
                    if ">" in condition or "<" in condition:  # "s<1351:px"
                        if ">" in condition:
                            op = ">"
                        else:
                            op = "<"
                        
                        condition = condition.split(op)
                        variable = condition[0]
                        value = condition[1]

                        parsed_rules.append({
                            "variable": variable,
                            "value": value,
                            "op": op,
                            "next_w": next_w}
                        )
                else:  # "A", "R" or next workflow
                    parsed_rules.append(rule)
            workflows[w_name] = parsed_rules
        
        elif not is_workflow:
            part_values = {}
            var_values = line[1:-1].split(",")
            for var_value in var_values:
                var_value = var_value.split("=")
                part_values[var_value[0]] = var_value[1]
            parts.append(part_values)
            
    return workflows, parts


def count_part_rating(part: dict, is_accepted: bool) -> int:
    return sum(int(val) for val in part.values()) if is_accepted else 0


def apply_rules(workflows: dict, part: dict, initial_workflow: str = "in", rule_index: int = 0) -> int:
    if initial_workflow in ["A", "R"]:
        rating = count_part_rating(part, is_accepted=True if initial_workflow == "A" else False)
        print(f" -> {initial_workflow} [{rating}]")
        return rating
    
    workflow = workflows[initial_workflow]
    rule = workflow[rule_index]
    if isinstance(rule, dict):
        variable = rule["variable"]
        value = int(rule["value"])
        op = rule["op"]
        next_w = rule["next_w"]
        if op == ">":
            if int(part[variable]) > value:
                return apply_rules(workflows, part, next_w, 0)
            else:
                return apply_rules(workflows, part, initial_workflow,  rule_index + 1)
        elif op == "<":
            if int(part[variable]) < value:
                return apply_rules(workflows, part, next_w, 0)
            else:
                return apply_rules(workflows, part, initial_workflow,  rule_index + 1)
    
    elif rule == "A":
        rating = count_part_rating(part, is_accepted=True)
        print(f" -> A [{rating}]")
        return rating
    
    elif rule == "R":
        print(" -> R")
        return 0
    
    else:
        next_w = rule
        print(f" -> {next_w}", end="")
        return apply_rules(workflows, part, next_w, 0)
    
    
def apply_rules_to_all(workflows: dict, parts: list) -> int:
    total = 0
    initial_workflow = "in"
    for part in parts:
        print(f"{part} -> {initial_workflow}", end="")
        total += apply_rules(workflows, part, initial_workflow, 0)
    return total
    

if __name__ == "__main__":
    w, p = process_input(read_input(load_dummy=False))
    part1_sum = apply_rules_to_all(w, p)
    print(f"Part 1: {part1_sum}")
    
    

