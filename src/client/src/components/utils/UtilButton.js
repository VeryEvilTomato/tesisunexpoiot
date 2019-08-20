import React, { Component } from 'react'

export default class UtilButton extends Component {
    buttonHandler = () => {
        const { functionCallback } = this.props
        functionCallback(this.props.propContent)
    }
    render() {
        const { propContent } = this.props
        return (
            <button onClick={this.buttonHandler}>{propContent}</button>
        )
    }
}