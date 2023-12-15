from collections import defaultdict

from utils import read_input


DEBUG = False


def get_string_has_number(string: str) -> int:
    value = 0
    for char in string:
        ascii_val = ord(char)
        value += ascii_val
        value *= 17
        value %= 256
    return value


def part1():
    sum_hashes = 0
    for w in words:
        word_value = get_string_has_number(w)
        if DEBUG:
            print(f"{w} ==> {word_value}")
        sum_hashes += word_value
    print(f"Part 1 - total hash: {sum_hashes}")
    
    
def replace_focal_length(box: list, label: str, focal_length: str):
    for i in range(len(box)):
        if box[i][0] == label:
            box[i][1] = focal_length


def add(label: str, f: str, box_number: int, boxes: dict[int, list], boxes_labels: dict[int, set]) -> None:
    if label in boxes_labels[box_number]:
        replace_focal_length(boxes[box_number], label, f)
    else:
        boxes_labels[box_number].add(label)
        boxes[box_number] += [[label, f]]
        

def remove(label: str, box_number: int, boxes: dict[int, list], boxes_labels: dict[int, set]) -> None:
    if label in boxes_labels[box_number]:
        boxes_labels[box_number].remove(label)
        for lenses in boxes[box_number]:
            if lenses[0] == label:
                boxes[box_number].remove(lenses)
        # clean up empty boxes
        if len(boxes_labels[box_number]) == 0:
            del boxes[box_number]
            del boxes_labels[box_number]
                
            
def print_boxes(boxes: dict) -> None:
    print("-------------------")
    for box in boxes:
        print(f"Box {box}: {boxes[box]}")
    
    
def part2():
    boxes = defaultdict(list)
    boxes_labels = defaultdict(set)
    for w in words:
        remove_lens = w[-1] == "-"
        label = w[:-1] if remove_lens else w.split("=")[0]
        f = w[-1] if not remove_lens else None
        box_number = get_string_has_number(label)
        
        if remove_lens:
            remove(label, box_number, boxes, boxes_labels)
        else:
            add(label, f, box_number, boxes, boxes_labels)
    
    if DEBUG:
        print_boxes(boxes)
    
    total = 0
    for box_number, box in boxes.items():
        for slot, lens in enumerate(box):
            power = (box_number + 1) * (slot + 1) * int(lens[1])
            total += power
            
    print(f"Part 2 - focusing power: {total}")
        

if __name__ == "__main__":
    words = read_input()[0].split(",")
    part1()
    part2()
