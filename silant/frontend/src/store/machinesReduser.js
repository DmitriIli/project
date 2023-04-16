const defaultState = {
    machines: [],
    verboseNames: []
}

export const machinesReduser = (state = defaultState, action) => {
    switch (action.type) {
        case "GETMACHINES":
            return { ...state, machines: [...state.machines, action.payload.context], verboseNames: [...state.verboseNames, action.payload.verboseNames] }
        default:
            return state
    }
    
}