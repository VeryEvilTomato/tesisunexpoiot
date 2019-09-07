import React, { Component } from 'react'
import { observer } from 'mobx-react'

import Monitor from './Monitor'

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
        }
    }
    render() {
        return (
            <div className='Panel'>
                <h2>{ this.props.uiState.device.name }</h2>
                {this.renderSwitch(this.props.uiState.selection)}
            </div>
        )
    }
})

export default panel
