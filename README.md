
# NOTES APPLICATION

The goal of this project is to develop a Python-based RESTful API for a simple note-taking application. The application allows the users to create, edit, manage and share their notes.


## Features

- **User Authentication**: To access their notes, users must safely register and log in.
- **Create Notes**: By entering a title and content, users can add new notes.

- **Edit Notes**: Users have the ability to make changes to their current notes.
- **Share Notes**: Users can share their notes with other users.
- **Version History**: Users are able to see their notes' version history, which includes all of the modifications made over time.
- **API Endpoints**: The application offers programmatic API endpoints for note interaction, facilitating system integration.


    
## Run Locally

Clone the project

```bash
  git clone https://github.com/kjlenish/Notes-Application.git
```


Install dependencies

```bash
  pip install -r requirements.txt
  ```

Start the Application

```bash
  python manage.py runserver
```


## API Reference

#### Signup

```http
  POST /signup/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. Your username |
| `password` | `string` | **Required**. Your password |

#### Login

```http
  POST /login/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. Your username |
| `password` | `string` | **Required**. Your password |

#### Create Note

```http
  POST /notes/create
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`      | `string` | **Required**. Title of the note |
| `content`      | `string` | **Required**. Content |

#### Get Note

```http
  GET /notes/{id}
```

#### Update Note

```http
  PUT /notes/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`      | `string` | **Required**. Title of the note |
| `content`      | `string` | **Required**. Content |
| `created_by` | `int` | **Required**. pk of user |


#### Share Note

```http
  POST /notes/{id}/share
```

#### Get Note version history

```http
  GET /notes/version-history/{id}
```


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://kjlenish.github.io/Visit-my-Portfolio/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kjlenish)

