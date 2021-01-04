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
def race_team(hero):
    team_members_nmb = 3
    test_team = CreateTeam('Test Name', hero['race'], team_members_nmb)
    race_team = test_team.get_team_of_race()
    return race_team


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
def test_number_of_membres_in_race_team_of_heroes(race_team):
    assert len(race_team) == 3
