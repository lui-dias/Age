from age.entity import Entity, Skill, AttackType

class Warrior(Entity):
    @property
    def skills(self):
        return [
            Skill(
                name          = 'Basic attack',
                attack_type   = AttackType.PHYSIC,
                attack_damage = 10,
                cooldown      = 0,
                magic_power   = 0,
                wait_turns    = 0,
                description   = 'Basic attack',
            ),
            Skill(
                name          = 'Charged Attack',
                attack_type   = AttackType.PHYSIC,
                attack_damage = 40,
                cooldown      = 0,
                magic_power   = 0,
                wait_turns    = 1,
                description   = 'The warrior charges his attack for 1 turn, and then strikes a powerful attack, causing a lot of damage',
            ),
        ]

class Mage(Entity):
    @property
    def skills(self):
        return [
            Skill(
                name          = 'Basic attack',
                attack_type   = AttackType.PHYSIC,
                attack_damage = 10,
                cooldown      = 0,
                magic_power   = 0,
                wait_turns    = 0,
                description   = 'Basic attack',
            ),
            Skill(
                name          = 'Fireball',
                attack_type   = AttackType.MAGIC,
                attack_damage = 0,
                cooldown      = 0,
                magic_power   = 20,
                wait_turns    = 0,
                description   = 'Throw a fireball at the enemy',
            )
        ]

class Dummy(Entity):
    ...

class Slime(Entity):
    ...