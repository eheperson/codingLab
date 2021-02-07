function [xs, ts, xi] = prep(x,t,delay)

    s = size(x);
    sdata = s(2);
    
    for i = 1:sdata-delay
        xs(1,i) = x(i+delay);
        xs(2,i) = t(i+delay);
        ts(1,i) = t(i+delay);
    end
    
    for i = 1: delay
        xi(1,i) = x(i);
        xi(2,i) = t(i);
    end
end