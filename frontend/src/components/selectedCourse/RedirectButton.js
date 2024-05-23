import React from 'react'
import { motion } from "framer-motion";
import { useEffect, useRef } from "react";
import { Link } from 'react-router-dom';

function RedirectButton() {
    return (
        <div className="flex min-h-[200px] items-center justify-center px-4"
            style={{background: 'lavender'}}
        >
          <SpotlightButton />
        </div>
    );
}

const SpotlightButton = () => {
    const btnRef = useRef(null);
    const spanRef = useRef(null);
  
    useEffect(() => {
      const handleMouseMove = (e) => {
        const { width } = e.target.getBoundingClientRect();
        const offset = e.offsetX;
        const left = `${(offset / width) * 100}%`;
  
        spanRef.current.animate({ left }, { duration: 250, fill: "forwards" });
      };
  
      const handleMouseLeave = () => {
        spanRef.current.animate(
          { left: "50%" },
          { duration: 100, fill: "forwards" }
        );
      };
  
      const btn = btnRef.current;
        if (btn) {
            btn.addEventListener('mousemove', handleMouseMove);
            btn.addEventListener('mouseleave', handleMouseLeave);
        }

        return () => {
            if (btn) {
                btn.removeEventListener('mousemove', handleMouseMove);
                btn.removeEventListener('mouseleave', handleMouseLeave);
            }
        };
    }, []);
  
    return (
      <motion.button
        whileTap={{ scale: 0.985 }}
        ref={btnRef}
        className="relative w-full max-w-xs overflow-hidden rounded-lg bg-blue-950 px-4 py-3 text-lg font-medium text-white"
      >
        <span className="pointer-events-none relative z-10 mix-blend-difference">
          I Wanna Learn!
        </span>
        <span
          ref={spanRef}
          className="pointer-events-none absolute left-[50%] top-[50%] h-32 w-32 -translate-x-[50%] -translate-y-[50%] rounded-full bg-slate-100"
        />
      </motion.button>
    );
  };

export default RedirectButton