import React, { Component } from 'react'
import { observer } from 'mobx-react'

import Monitor from './monitor/Monitor'

const panel = observer(class panel extends Component {
    renderSwitch(selection){
        switch (selection) {
            case "monitors":
                return <Monitor 
                            device={this.props.uiState.device}
                            uiState={this.props.uiState}
                        />
            case "controls":
                return <div>Control placeholder</div>
            default:
                return ""
        }
    }
    render() {
        return (
            <div className='Panel'>
                {this.renderSwitch(this.props.uiState.selection)}
            </div>
        )
    }
})

export default panel
