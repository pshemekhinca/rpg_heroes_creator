import pytest
from heroes import Hero, CreateTeam
from unittest import expectedFailure


@pytest.fixture()
def hero():
    sample = Hero('shifter')
    return sample.get_hero()


@pytest.fixture()
def hero2():
    sample2 = Hero('human')
    return sample2.get_hero()


@pytest.fixture()
def team_1(hero):
    team_members_nmb = 3
    test_team = CreateTeam('Test Name', hero['race'], team_members_nmb)
    team_1 = test_team.get_team()
    return team_1


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


@pytest.mark.parametrize('data, expected', [
    ('power', 100),
    ('agile', 100),
    ('durability', 100),
])
def test_get_starting_hero_attribute(data, expected, hero):
    attr = hero[f'{data}']
    assert attr == expected


# @pytest.mark.skip()
def test_create_team_of_heroes(team_1):
    assert len(team_1) == 3
