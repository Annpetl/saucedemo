import allure
import pytest


@allure.feature('Random dog')
@allure.story('Полученсие фото лучайной собаки')
def test_random_dog(dog_api):
    response = dog_api.get('breeds/image/random')

    with allure.step('проверка кода ответа'):
        assert response.status_code == 200, f'Ожидаемый статус код: 200, получен {response.status_code}'


@pytest.mark.parametrize("breed", [
    "afghan",
    "basset",
    "blood",
    "english",
    "ibizan",
    "plott",
    "walker"
])
def test_get_random_breed_image(dog_api, breed):
    response = dog_api.get(f'breed/hound/{breed}/images/random')
    with allure.step("Запрос отправлен. Десериализируем ответ из json в словарь."):
        response = response.json()
    print(response)
    assert breed in response['message'], f'нет ссылки на изображение с указанной породой, ответ {response}'




@allure.feature('List of dog images')
@allure.story('Список всех фото собак списком содержит только изображения')
@pytest.mark.parametrize("file", ['.md', '.MD', '.exe', '.txt'])
def test_get_breed_images(dog_api, file):
    response = dog_api.get("breed/hound/images")
    response = response.json()
    result = '\n'.join(response["message"])
    assert file not in result, f'В сообщении есть файл с расширением {file}'


@allure.feature('List of dog images')
@allure.story('Список фото определенных пород')
@pytest.mark.parametrize("breed", [
    "african",
    "boxer",
    "entlebucher",
    "elkhound",
    "shiba",
    "whippet",
    "spaniel",
    "dvornyaga"
])
def test_get_random_breed_images(dog_api, breed):
    response = dog_api.get(f"breed/{breed}/images/")
    response = response.json()


@allure.feature('List of dog images')
@allure.story('Список определенного количества случайных фото')
@pytest.mark.parametrize("number_of_images", [i for i in range(1, 10)])
def test_get_few_sub_breed_random_images(dog_api, number_of_images):
    response = dog_api.get(f"breed/hound/afghan/images/random/{number_of_images}")
    response = response.json()
    print(response["message"])
    final_len = len(response["message"])
    assert final_len == number_of_images, f"Количество фото не {number_of_images}, а {final_len}"
