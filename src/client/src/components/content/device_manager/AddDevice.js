import React, { Component } from 'react'

import { observer } from 'mobx-react'

import './AddDevice.css'

const AddDevice = observer(class AddDevice extends Component {
    constructor(props) {
        super(props);
        this.state = {
            name: "",
            variable: this.props.uiState.options.variables[0],
            type: this.props.uiState.options.types[0].request
        }
    }
    typeHandler = (e) => { this.setState({type: e.target.value}) }
    variableHandler = (e) => {this.setState({variable: e.target.value})}
    nameHandler = (e) => {
        if(e.target.value.length > 30) {
            alert("El nombre debe de ser menor a 30 caracteres");
            return
        }
        this.setState({name: e.target.value.trim()})
    }
    submitHandler = (e) => {
        e.preventDefault()
        if(this.state.name.length > 0 || this.state.variable !== "" || this.state.type !== "") {
            this.props.uiState.submitDevice({
                "jsonData": {
                    "name": this.state.name,
                    "variable": this.state.variable
                },
                "request": this.state.type
            })
        }
        else { alert("Debe llenar todos los campos") }
    }
    optionHandler = (option) => { this.props.uiState.managerSelection = option }
    render() {
        return (
            <div className="AddRemove">
                {this.props.uiState.options === null ?
                    <h1>Cargando</h1>
                    :
                    <div className="container">
                        <form className="formClass" onSubmit={this.submitHandler}>
                            <h3>Agregar nuevo dispositivo:</h3>
                            <p><b>Introduzca el nombre:</b>
                                <input
                                    id="formName"
                                    type="text"
                                    value={this.state.name}
                                    onChange={this.nameHandler}
                                    placeholder="Escriba el nombre aquí"
                                />
                            </p>
                            {this.state.type === "switches" ? "" :
                                <p><b>Seleccione la variable</b>
                                    <select
                                        id="formVariable"
                                        value={this.state.variable}
                                        onChange={this.variableHandler}
                                    >
                                    {this.props.uiState.options.variables.map((variable) => {
                                        return <option value={variable}>{variable}</option>
                                    })}
                                    </select>
                                </p>
                            }
                            <p><b>Seleccione el tipo:</b>
                                <select
                                    id="formType"
                                    value={this.state.type}
                                    onChange={this.typeHandler}
                                >
                                {this.props.uiState.options.types.map((type) => {
                                    return <option value={type.request}>{type.name}</option>
                                })}
                                </select>
                            </p>
                            <p>
                                <input
                                    id="formSubmit"
                                    type="submit"
                                    value="Agregar dispositivo"
                                />
                            </p>
                        </form>
                        <button onClick={() => { this.optionHandler(null) } }>Regresar al menú anterior</button>
                    </div>
                }
            </div>
        )
    }
})

export default AddDevice