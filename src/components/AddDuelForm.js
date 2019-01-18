import React from "react";
import {Form, Button, Select} from "antd";
import {connect} from "react-redux";
import axios from "axios";

const FormItem = Form.Item;


class AddDuelForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            user1: null,
            dataset: null
        };
        this.handleUserChange = this.handleUserChange.bind(this)
        this.handleUserDataset = this.handleUserDataset.bind(this)
    }


    handleFormSubmit = async (event, requestType, duelID) => {
        event.preventDefault();

        const postObj = {
            user1: this.state.user1,
            dataset: this.state.dataset,
        };
        console.log(postObj)
        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
        axios.defaults.xsrfCookieName = "csrftoken";
        axios.defaults.headers = {
            "Content-Type": "application/json",
            Authorization: `Token ${this.props.token}`,
        };

        if (requestType === "post") {
            await axios.post("http://127.0.0.1:8000/api/duel/create/", postObj)
                .then(res => {
                    if (res.status === 201) {
                        this.props.history.push(`/`);
                    }
                })
        } else if (requestType === "put") {
            await axios.put(`http://127.0.0.1:8000/api/duel/${duelID}/update/`, postObj)
                .then(res => {
                    if (res.status === 200) {
                        this.props.history.push(`/`);
                    }
                })
        }
    };

    handleUserChange(value) {
        this.setState({user1: value})
    }

    handleUserDataset(value) {
        this.setState({dataset: value})
    }

    render() {
        return (
            <div>
                <Form
                    onSubmit={event =>
                        this.handleFormSubmit(
                            event,
                            this.props.requestType,
                            this.props.articleID
                        )
                    }
                >
                    <FormItem label="User"><Select name="user1" onChange={this.handleUserChange}>
                        {this.props.users.map(user => <Select.Option
                            value={user.id}>{user.username}</Select.Option>)}
                    </Select></FormItem>

                    <FormItem label="Dataset"><Select name="dataset" onChange={this.handleUserDataset}>
                        {this.props.datasets.map(dataset => <Select.Option
                            value={dataset.id}>{dataset.name}</Select.Option>)}
                    </Select></FormItem>

                    <FormItem>
                        <Button type="primary" htmlType="submit">
                            {this.props.btnText}
                        </Button>
                    </FormItem>
                </Form>
            </div>
        );
    }
}

const mapStateToProps = state => {
    return {
        token: state.token
    };
};

export default connect(mapStateToProps)(AddDuelForm);