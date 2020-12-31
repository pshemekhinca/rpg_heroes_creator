import pytest
from heroes import Hero, get_hero_of_race
from unittest import expectedFailure


@pytest.fixture()
def hero():
    sample = Hero('shifter', get_hero_of_race(3))
    return sample.get_hero()


@pytest.fixture()
def hero2():
    sample2 = Hero('human', get_hero_of_race(0))
    return sample2.get_hero()


def test_hero_instance_created_as_dictionary(hero):
    assert type(hero) == dict


@pytest.mark.parametrize('data, expected', [
    ('name', True),
    ('race', True),
    ('items', True),
    ])
def test_heroes_created_with_random_atributes(data, expected, hero, hero2):
    result = (hero[f'{data}'] != hero2[f'{data}'])
    assert result == expected


