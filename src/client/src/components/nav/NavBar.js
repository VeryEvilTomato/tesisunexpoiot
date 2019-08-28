import React, { Component } from 'react'
import { observer } from 'mobx-react'

import './NavBar.css'

const NavBar = observer (class NavBar extends Component {
    render() {
        return (
            <div className='NavBar'>
                <div id="logo">Logo</div>
                <button onClick={() => console.log("Agregar dispositivo")}
                >Agregar dispositivo</button>
                <button onClick={() => {
                            this.props.uiState.setContent(
                                "monitors", 
                                "Lista de monitores"
                            )
                        } 
                    }
                >Lista de monitores</button>
                <button onClick={() => console.log("Lista de controles")}
                >Lista de controles</button>
                <button onClick={() => console.log("Abandonar sesión")}
                >Abandonar sesión</button>
            </div>
        )
    }
})

export default NavBar