import React, { Component } from 'react'
import { observer } from 'mobx-react'
import logo from './unexpo_logo.svg'

import './NavBar.css'

const NavBar = observer(class NavBar extends Component {
    render() {
        return (
            <div className='NavBar'>
                <div className='container'>
                    <img id="logo" src={logo} alt="Logo de la universidad" ></img>
                </div>
                <button onClick={() => {
                        this.props.uiState.setDevicemanager();
                    }
                }
                >Gestor de dispositivos</button>
                <button onClick={() => {
                            this.props.uiState.setContent("monitors", "Lista de monitores")
                        }
                    }
                >Lista de monitores</button>
                <button onClick={() => {
                            this.props.uiState.setContent("switches", "Lista de interruptores")
                        }
                    }
                >Lista de interruptores</button>
                <button onClick={() => this.props.uiState.cleanSession()}
                >Abandonar sesión</button>
            </div>
        )
    }
})

export default NavBar