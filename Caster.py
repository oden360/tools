## This Casts items to an output  



class Caster:
    @staticmethod
    def cast(data):
        if isinstance(data, dict):
            return CustomData.from_dict(data)
        return None