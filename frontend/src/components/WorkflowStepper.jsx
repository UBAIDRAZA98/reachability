import React from 'react';

const steps = [
  "REGISTERED", "VERIFIED", "ASSESSED", "APPROVED", "AUDITED (S6)"
];

export default function WorkflowStepper({ currentStepIndex = 0 }) {
  return (
    <div style={{ display: 'flex', justifyContent: 'space-between', margin: '2rem 0' }}>
      {steps.map((step, index) => {
        const isActive = index <= currentStepIndex;
        return (
          <div key={step} style={{ textAlign: 'center', flex: 1, position: 'relative' }}>
            {/* Circle */}
            <div style={{
              width: '30px', height: '30px', borderRadius: '50%',
              backgroundColor: isActive ? '#2563eb' : '#e5e7eb',
              color: 'white', display: 'flex', alignItems: 'center', justifyContent: 'center',
              margin: '0 auto 10px', fontWeight: 'bold', zIndex: 2, position: 'relative'
            }}>
              {index + 1}
            </div>
            
            {/* Line connector */}
            {index < steps.length - 1 && (
              <div style={{
                position: 'absolute', top: '15px', left: '50%', width: '100%', height: '2px',
                backgroundColor: index < currentStepIndex ? '#2563eb' : '#e5e7eb',
                zIndex: 1
              }} />
            )}

            <span style={{ fontSize: '12px', color: isActive ? '#0f172a' : '#94a3b8', fontWeight: isActive ? '600' : '400' }}>
              {step}
            </span>
          </div>
        );
      })}
    </div>
  );
}
