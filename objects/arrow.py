class arrow:
    placement = {"before" : 0, "after": 1}
    arrow_types = [{"style": "--><-", "length": 5},
                     {"style": "-><--", "length": 5},
                     {"style": "-><-", "length": 4},
                     {"style": "->", "length": 2},
                     {"style": "<-", "length": 2}]
    """
    arrow_types = [{"first_part":"-->", "last_part": "<-", "caption_start_index": 3, "lenght_after_caption": 2},
                   {"first_part":"->", "last_part": "<--", "caption_start_index": 2, "lenght_after_caption": 3},
                   {"first_part":"->", "last_part": "<-", "caption_start_index": 2, "lenght_after_caption": 2},
                   {"first_part":"-", "last_part": ">", "caption_start_index": 1, "lenght_after_caption": 1},
                   {"first_part":"<", "last_part": "-", "caption_start_index": 1, "lenght_after_caption": 1}]
    """
    def __init__(self, arrow_type, index, caption_before = "", caption_after = ""):
        self.type = arrow_type
        self.caption = {"before": caption_before,
                         "after": caption_after}
        self.index = index

    def caption_index_range(self):
        before_start_index = self.index - len(self.caption["before"])
        before_end_index = self.index
        after_start_index = self.index + len(self.type)
        after_end_index = after_start_index + len(self.caption["after"])
        
        return {"before":{"start_index": before_start_index, "end_index": before_end_index}, 
                "after":{"start_index": after_start_index, "end_index": after_end_index}
                }

    def total_length(self): # This length includes the arrow and its captions
        caption_range = self.caption_index_range()
        before_caption_length = caption_range["before"]["end_index"] - caption_range["before"]["start_index"]
        after_caption_length = caption_range["afer"]["end_index"] - caption_range["after"]["start_index"]
        return before_caption_length + len(self.type) + after_caption_length
