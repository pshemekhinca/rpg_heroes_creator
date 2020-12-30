import pytest
from heroes import Hero, get_hero_of_race
from unittest import expectedFailure


@pytest.fixture()
def hero():
    create_kind = 'shifter'
    sample = Hero(get_hero_of_race(create_kind), create_kind)
    return sample.get_hero()


@pytest.fixture()
def hero2():
    create_kind = 'shifter'
    sample2 = Hero(get_hero_of_race(create_kind), create_kind)
    return sample2.get_hero()


def test_hero_instance_created_as_dictionary(hero):
    assert type(hero) == dict


@pytest.mark.parametrize('data, expected', [
    ('name', True),
    ('items', True),
    ])
def test_heroes_created_with_different_random_name(data, expected):
    result = (hero[f'{data}'] != hero2[f'{data}'])
    assert result == expected


def test_random_list_of_item_for_each_hero(hero, hero2):
    assert hero['items'] != hero2['items']

