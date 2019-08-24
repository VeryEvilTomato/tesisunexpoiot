import React, { Component } from 'react'
import UtilButton from '../helpers/UtilButton'

import './NavMenu.css'

export default class NavMenu extends Component {
    render() {
        return (
            <div className="NavMenu">
                <UtilButton
                    id='NavButton'
                    functionCallback={() => console.log("En proceso - Agregar dispositivo")}
                    contentType='Agregar nuevo dispositivo'
                />
                <UtilButton
                    id='NavButton'
                    functionCallback={this.props.contentTypeHandler}
                    request='/monitors'
                    contentType='Lista de monitores'
                />
                <UtilButton
                    id='NavButton'
                    functionCallback={this.props.contentTypeHandler}
                    request='/controls'
                    contentType='Lista de controles'
                />
                <UtilButton
                    id='NavButton'
                    functionCallback={this.props.logoffHandler}
                    request='/logoff'
                    contentType='Abandonar sesión'
                />
            </div>
        )
    }
}