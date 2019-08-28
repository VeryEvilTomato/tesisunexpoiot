import React, { Component } from 'react'
import { observer } from 'mobx-react'

import './Content.css'

const Content = observer (class Content extends Component {
    render() {
        return (
            <div className='Content'>
                <h1>{this.props.uiState.selectionText}</h1>
                {
                    this.props.uiState.content.map((device) =>
                        <div className='device'>
                            <p>{device.name}</p>
                            <p>{device.variable}</p>
                        </div>
                    )
                }
            </div>
        )
    }
})

export default Content