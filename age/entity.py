from enum import Enum, auto
from dataclasses import dataclass, field


class Calculate:
    def physic_damage(damage: int, armor: int):
        return damage * (100 / (100 + armor))

    def magical_damage(damage: int, armor: int):
        return damage * (100 / (100 + armor))


class AttackType(Enum):
    PHYSIC = auto()
    """ Physical attack """
    MAGIC  = auto()
    """ Magical attack """


@dataclass
class Skill:
    attack_damage: int
    """ The amount of damage the atack basic does """
    cooldown     : int
    """ The cooldown of the skill in seconds """
    magic_power  : int
    """ The amount of magic power the skill has """
    name         : str
    """ The name of the skill """
    attack_type  : AttackType
    """ The type of attack the skill is """
    description  : str
    """ The description of the skill """
    wait_turns : int
    """ The number of turns the skill needs to wait to be used """

@dataclass
class Attack:
    damage  : int
    """
    The sum of the total damage, e.g.
    If the skill causes 100 MP (+10% MP)

    The damage is 100 MP (+10% MP), not only 100 MP
    """
    attacker: 'Entity'
    """ The entity that attacks """
    defender: 'Entity'
    """ The entity that is attacked """
    skill   : Skill
    """ The skill the attacker used to attack """

@dataclass
class Entity:
    armor           : int
    """ The amount of armor the entity has """
    attack_damage   : int
    """ The amount of damage the entity basic does """
    health          : int
    """ The amount of actual health the entity has """
    max_health      : int  = field(init=False)
    """ The maximum amount of health the entity has """
    id              : int
    """ The id of the entity """
    magic_power     : int
    """ The amount of magic power the entity has """
    magic_resistance: int
    """ The amount of magic resistance the entity has """
    name            : str
    """ The name of the entity """

    def __post_init__(self):
        self.max_health = self.health

    @property
    def skills(self):
        """
        Returns all skills the entity has
        """

        return []

    @property
    def is_dead(self):
        return self.health == 0

    def _calculate_damage(self, defender: 'Entity', skill: Skill):
        """ Calculates the damage received from an entity """

        return round(
            Calculate.physic_damage(self.attack_damage, defender.armor)
            if skill.attack_type == AttackType.PHYSIC
            else Calculate.magical_damage(self.magic_power, defender.magic_resistance)
        )

    async def hit(self, defender: 'Entity', skill: Skill):
        """
        Attacks an entity

        Returns the attack information 
        """

        damage = self._calculate_damage(defender, skill)
        defender.health -= max(0, damage)
        return Attack(damage, self, defender, skill)