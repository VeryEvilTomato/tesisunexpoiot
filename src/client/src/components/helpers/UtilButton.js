import React, { Component } from 'react'
import './UtilButton.css'

export default class UtilButton extends Component {
    buttonHandler = () => {
        this.props.functionCallback(this.props)
    }
    render() {
        const { contentType } = this.props
        return (
            <button id={this.props.id} onClick={this.buttonHandler}>{contentType}</button>
        )
    }
}