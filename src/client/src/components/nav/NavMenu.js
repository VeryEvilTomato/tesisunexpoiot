import React, { Component } from 'react'
import UtilButton from '../utils/UtilButton'

import './NavMenu.css'

export default class NavMenu extends Component {
    render() {
        return (
            <div className="NavMenu">
                <UtilButton functionCallback={this.props.contentHandler} propContent='Monitores' />
                <UtilButton functionCallback={this.props.contentHandler} propContent='Controles' />
                <UtilButton functionCallback={this.props.logoffHandler} propContent='Abandonar sesión' />
            </div>
        )
    }
}