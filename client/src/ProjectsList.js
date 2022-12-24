import React from 'react';
import './ProjectList.css';

export default class ProjectsList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            items: []
        };
    }

    componentDidMount() {
        fetch("http://127.0.0.1:8008/api/projects")
            .then(res => res.json())
            .then(
                (result) => {
                    console.log("yes");
                    this.setState({
                        isLoaded: true,
                        items: result
                    });
                },
                // Примечание: важно обрабатывать ошибки именно здесь, а не в блоке catch(),
                // чтобы не перехватывать исключения из ошибок в самих компонентах.
                (error) => {
                    console.log("no");
                    this.setState({
                        isLoaded: true,
                        error
                    });
                }
            )
    }

    render() {
        const {error, isLoaded, items} = this.state;
        if (error) {
            return <div>Ошибка: {error.message}</div>;
        } else if (!isLoaded) {
            return <div>Загрузка...</div>;
        } else {
            return (
                <ul>
                    {items.map(item => (
                        <li key={item.id}>
                            {item.title}
                            <ul>
                                <li>Владелец: {item.owner}</li>
                                <li>Менеджер: {item.manager}</li>
                                <li>Стоимость проекта: {item.price}</li>
                                <li>Статус: {item.status}</li>
                            </ul>
                        </li>
                    ))}
                </ul>
            );
        }
    }
}
