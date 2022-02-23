class School:
    def __init__(self, name, level, numberOfStudents):
        self._name = name
        self._level = level
        self._numberOfStudents = numberOfStudents

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def get_numberOfStudents(self):
        return self._numberOfStudents

    def set__numberOfStudents(self, value: float):
        self._numberOfStudents = value
        return self._numberOfStudents

    def __repr__(self):
        return f'The {self._level} school {self._name} contains {self._numberOfStudents}'


class Primary(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, 'primary', numberOfStudents)
        self.pickupPolicy = pickupPolicy

    def get_primary(self):
        return self.pickupPolicy

    def __repr__(self):
        return f'{super().__repr__()} with the pickup policy {self.pickupPolicy}'


class Middle(School):
    pass


class HighSchool(School):
    def __init__(self, name, numberOfStudents, sportsTeams=[]):
        super().__init__(name, 'high', numberOfStudents)
        self.sportsTeams = sportsTeams

    def get_high(self):
        return self.sportsTeams

    def __repr__(self):
        if self.sportsTeams:
            if len(self.sportsTeams) > 1:
                return f'{super().__repr__()} with the teams: ' \
                       f"{', '.join(self.sportsTeams)}."
            else:
                return f'{super().__repr__()} with the team: ' \
                       f'{", ".join(self.sportsTeams)}'
        else:
            return f'{super().__repr__()}'


sch = HighSchool("'Lviv'", 1500, ['TEAM', 'TEAM_2'])
prim = Primary("'Name'", 1600, 'PickUpPolicy')
print(sch)
print(prim)
print(sch.get_numberOfStudents())
print(sch.set__numberOfStudents('1700'))
print(sch.get_numberOfStudents())