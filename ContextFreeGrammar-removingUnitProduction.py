class ContextFreeGrammar():
    def __init__(self, production):
        """
        we suposed to get an valid CFG production and then remove it unit products
        :param production: dictionary
        """
        self.cfg = production.copy()

    def remove_unit_production(self):
        while self.has_unit_production(self.cfg):
            self.cfg = self.check_unit_production(self.cfg)

    def is_unit_production(self, rule):
        return len(rule) == 1 and rule[0].isupper()  # its one variable

    def has_unit_production(self, cfg):
        for rules in cfg.values():
            for rule in rules:
                if self.is_unit_production(rule):
                    return True

        return False

    def check_unit_production(self, cfg):
        newRule_T = []
        newRule = dict()
        for var, rules in cfg.items():
            flag = False
            for rule in rules:
                if self.is_unit_production(rule):
                    newRule_T = [item for item in cfg[rule] + cfg[var] if
                                 item != var]  # adding what that unit variable made
                    try:
                        newRule_T.remove(rule)  # removing the unit variable itself
                    except ValueError:
                        pass
                    newRule_T = list(set(newRule_T))  # deleting the doubled item
                    newRule[var] = newRule_T  # making it a cfg type grammar again
                    flag = True
            if not flag:  # if there was no unit production
                newRule[var] = cfg[var]
        return newRule

    def input_cfg(self):
        made_cfg = dict()
        while True:
            line = input().strip()
            if not line:
                break
            else:
                try:
                    var, rules = line.split('->')
                except ValueError:
                    print('Invalid format')
                    continue
                rules = rules.split('|')
                made_cfg[var] = [rule for rule in rules]

        return made_cfg

    def print_cfg(self):
        for var, rules in self.cfg.items():
            print(f"{var} -> ", ' | '.join(rules))
        print('-' * 20)

    def set_cfg(self, cfg=None):
        if cfg:
            self.cfg = cfg
        else:
            self.cfg = self.input_cfg()

    def get_cfg(self):
        return self.cfg.copy()


def main():
    cfg = {
        'S': ['Aa', 'B', 'C'],
        'B': ['A', 'bb'],
        'A': ['a', 'bc', 'B'],
        'C': ['abc', 'efg', 'C']
    }
    CFG = ContextFreeGrammar(cfg)
    print('CF rules before removing is :')
    CFG.print_cfg()
    CFG.remove_unit_production()
    print('CF rules after removing is :')
    CFG.print_cfg()

if __name__ == '__main__':
    main()