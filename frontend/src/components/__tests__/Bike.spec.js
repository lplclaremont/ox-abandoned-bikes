import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import Bike from '../Bike/Bike.vue'

describe('Bike', () => {
    it('renders properly with correct details', () => {
        const wrapper = mount(Bike, {
        props: {
            brand: 'Raleigh',
            condition: 'poor',
            date_found: '22-02-23',
            location_name: 'Test Location!'
        }})

        expect(wrapper.text()).toContain('Raleigh')
        expect(wrapper.text()).toContain('Condition, poor')
        expect(wrapper.text()).toContain('Found on 22-02-23')
        expect(wrapper.text()).toContain('Test Location!')
    })
})
