import React, { Component } from 'react'
import { observer } from 'mobx-react'

import './Auth.css'

const Auth = observer(class Auth extends Component {
    constructor(props) {
        super(props);
        this.state = {
            username: "",
            password: ""
        }
    }
    loginHandler = (e) => {
        e.preventDefault()
        this.props.uiState
        .userLogin(this.state.username, this.state.password)
        this.setState({ username:"", password:"" })
    }
    registerHandler = (e) => {
        e.preventDefault()
        this.props.uiState
        .userRegister(this.state.username, this.state.password)
        this.setState({ username:"", password:""})
    }
    usernameHandler = (e) => {
        e.preventDefault();
        const username = e.target.value;
        if(this.checkStr(username)) return;
        this.setState({username: username});
    }
    passwordHandler = (e) => {
        e.preventDefault();
        const password = e.target.value;
        if(this.checkStr(password)) return;
        this.setState({password: password})
    }
    checkStr(str) {
        let regexp = /[-:*/ +]/gi;
        if(str.search(regexp) !== -1) {
            alert("Por favor no utilizar los caracteres - : * / + [Espacio]")
            return true;
        }
        if(str.length > 16) {
            alert("No utilizar más de 16 caracteres por favor");
            return true;
        }
        else return false
    }
    switchType = (type) => {
        let { logState } = this.props.uiState 
        if (logState !== null) {
            switch(logState) {
                case "login":
                    return <div className="login">
                        <form
                            className="loginForm"
                            onSubmit={this.loginHandler}
                        >
                            <p><b>Usuario:</b></p>
                            <input
                                id="formUsername"
                                type="text"
                                value={this.state.username}
                                onChange={(e) => {this.setState({username: e.target.value})}}
                            />
                            <p><b>Contraseña:</b></p>
                            <input
                                id="formPassword"
                                type="text"
                                value={this.state.password}
                                onChange={(e) => {this.setState({password: e.target.value})}}
                            />
                            <input
                                type="submit"
                                value="Iniciar sesión"
                            />
                        </form>
                        <button onClick={() => {
                            this.setState({username:"", password:"" })
                            this.props.uiState.logState = null
                        }}>Regresar</button>
                    </div>
                case "register":
                    return <div className="register">
                        <form
                            className="loginForm"
                            onSubmit={this.registerHandler}
                        >
                            <p><b>Usuario:</b></p>
                            <input
                                id="formUsername"
                                type="text"
                                value={this.state.username}
                                onChange={this.usernameHandler}
                            />
                            <p><b>Contraseña:</b></p>
                            <input
                                id="formPassword"
                                type="text"
                                value={this.state.password}
                                onChange={this.passwordHandler}
                            />
                            <input
                                type="submit"
                                value="Registrar usuario"
                            />
                        </form>
                        <button onClick={() => {
                            this.setState({username:"", password:"" })
                            this.props.uiState.logState = null
                        }}>Regresar</button>
                    </div>
                default:
                    alert("Error")
                    return
            }
        }
    } 
    render() {
        return (
            <div className="Auth">
                { this.props.uiState.logState == null ? 
                    <div className="authMenu">
                        <button onClick={() => {this.props.uiState.logState = "login"}}>Iniciar sesión</button>
                        <button onClick={() => {this.props.uiState.logState = "register"}}>Registrarse</button>
                    </div>
                    :
                    <div className="type">
                        {this.switchType(this.state.type)}
                    </div>
                }
            </div>
        )
    }
})

export default Auth